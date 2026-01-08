"""Trade management for completed positions."""

class Trade:
    '''
    Represents a completed trade
    
    Attributes:
        ticker: Trading symbol.
        side: 'BUY' or 'SELL'.
        entry_price: Entry price.
        exit_price: Exit price.
        quantity: Number of units.
        entry_time: Entry timestamp (string or datetime).
        exit_time: Exit timestamp (string or datetime).
        pnl: Profit/Loss (calculated automatically).
        exit_reason: 'SL', 'TP', or 'MANUAL'.
    '''
    
    def __init__(self,
                 ticker: str,
                 side: str,
                 entry_price: float,
                 exit_price: float,
                 quantity: float,
                 entry_time: str,
                 exit_time: str,
                 exit_reason: str) -> None:
        
        """Initialize a completed trade and calculate P&L."""
        
        self.ticker = ticker
        self.side = side.upper()
        self.entry_price = entry_price
        self.exit_price = exit_price
        self.quantity = quantity
        self.entry_time = entry_time
        self.exit_time = exit_time
        self.exit_reason = exit_reason.upper()

        # Calculate P&L automatically
        self.pnl = self._calculate_pnl()
        
    def __str__(self):
        """
        User-friendly representation.

        Format: [WIN/LOSS] SIDE QUANTITY TICKER: ENTRY -> EXIT (REASON) | P&L: $X.XX
        Example: [WIN] BUY 10000 EURUSD: 1.0800 -> 1.0850 (TP) | P&L: $500.00
        """
        
        if self.is_winner() == True:
            result = '[WIN]'
        else:
            result = '[LOSS]'
            
        return (f'''{result} {self.side} {self.quantity} {self.ticker}: 
                {self.entry_price} -> {self.exit_price} ({self.exit_reason}) 
                | P&L: ${self.pnl:.2f}''')
    
    def __repr__(self):
        
        
        return (f'Trade(ticker = {self.ticker!r}, side = {self.side!r},'
                f'entry_price = {self.entry_price}, exit_price = {self.exit_price}'
                f'quantity = {self.quantity}, pnl = {self.pnl:.2f}, exit_reason = {self.exit_reason!r}'
        )
    
    def _calculate_pnl(self) -> float:
        """
        Calculate profit/loss based on side.

        Returns:
            P&L in currency units.
        """

        if self.side != 'BUY' and self.side != 'SELL':
            print('Incorrect side, it should be either BUY or SELL (case insensitive)')
            return None
        elif self.exit_price < 0 or self.entry_price < 0:
            print('Incorrect exit price or entry price, it should be above 0!')
            return None
        
        if self.side == 'BUY':
            pnl = (self.exit_price - self.entry_price) * self.quantity
            return pnl
        elif self.side == 'SELL':
            pnl = (self.entry_price - self.exit_price) * self.quantity
            return pnl
        
        
    def is_winner(self) -> bool:
        """Check if trade was profitable."""
        if self.pnl > 0:
            return True
        else:
            return False
        
    
    @classmethod
    def calculate_win_rate(cls, trades: list['Trade']) -> float:
        """
        Calculate win rate from list of trades.

        Args:
            trades: List of Trade objects.

        Returns:
            Win rate as percentage (0-100).
            Returns 0 if no trades.
        """

        if trades is not None:
            trades_profits = [trade._calculate_pnl() for trade in trades]
            winners = [profit for profit in trades_profits if profit > 0]
            print(trades_profits)
            return (len(winners) / len(trades_profits)) * 100
            
        else:
            return 0