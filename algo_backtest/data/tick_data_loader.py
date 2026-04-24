"""Tick data loader for AlgoBacktest — loads and indexes trade-level tick data."""

from typing import Optional
import pandas as pd
import logging

logger = logging.getLogger(__name__)


class TickDataLoader:
    """
    Loads raw tick data from CSV and indexes it by date for fast per-day access.

    The raw file schema:
        ts_recv, ts_recv_berlin, ts_event, price, size, side, symbol, instrument_id

    We keep only: date (from ts_recv_berlin), time (from ts_recv_berlin), price, side.
    Side values: 'B' = aggressive buyer (lifted ask), 'A' = aggressive seller (hit bid), 'N' = ignore.

    Attributes:
        file_path: Path to the raw CSV file.
        ticks_by_date: dict mapping date -> DataFrame(time, price, side), sorted by time.
    """

    def __init__(self, file_path: str) -> None:
        self.file_path = file_path
        self.ticks_by_date: dict[object, pd.DataFrame] = {}

    def __repr__(self) -> str:
        return f'TickDataLoader(file_path={self.file_path!r}, dates_loaded={len(self.ticks_by_date)})'

    def load_and_index(self) -> bool:
        """
        Load the CSV, parse the Berlin timestamp, and build a per-date index.

        Only keeps rows where side is 'B' or 'A' (drops 'N' and any other values).

        Returns:
            True if loading succeeded, False otherwise.
        """
        try:
            logger.info(f'Loading tick data from {self.file_path}...')
            df = pd.read_csv(
                self.file_path,
                usecols=['ts_recv_berlin', 'price', 'side'],
                dtype={'price': float, 'side': str},
            )

            df['ts_recv_berlin'] = pd.to_datetime(df['ts_recv_berlin'], utc=False)

            df = df[df['side'].isin(['B', 'A'])].copy()

            df['date'] = df['ts_recv_berlin'].dt.date
            df['time'] = df['ts_recv_berlin'].dt.time

            df = df[['date', 'time', 'price', 'side']].sort_values(['date', 'time'])

            for date, group in df.groupby('date'):
                self.ticks_by_date[date] = group[['time', 'price', 'side']].reset_index(drop=True)

            logger.info(f'Tick data indexed: {len(self.ticks_by_date)} trading days loaded.')
            return True

        except FileNotFoundError:
            logger.error(f'Tick data file not found: {self.file_path}')
            return False
        except Exception as e:
            logger.error(f'Failed to load tick data: {e}')
            return False

    def get_ticks_for_day(self, date: object) -> Optional[pd.DataFrame]:
        """
        Return the tick DataFrame for a given date, or None if not available.

        Args:
            date: datetime.date object.

        Returns:
            DataFrame with columns [time, price, side] sorted ascending by time, or None.
        """
        return self.ticks_by_date.get(date)

    def get_session_ticks(self, date: object, start, end) -> Optional[pd.DataFrame]:
        """
        Return ticks for a given date filtered to a session time window.

        Args:
            date: datetime.date object.
            start: datetime.time — session start (inclusive).
            end: datetime.time — session end (inclusive).

        Returns:
            Filtered DataFrame or None if no ticks for that date.
        """
        day_ticks = self.get_ticks_for_day(date)
        if day_ticks is None:
            return None
        mask = (day_ticks['time'] >= start) & (day_ticks['time'] <= end)
        result = day_ticks[mask].reset_index(drop=True)
        return result if not result.empty else None
