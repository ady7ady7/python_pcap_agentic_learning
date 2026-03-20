# python_pcap_agentic_learning

- THIS FILE WILL NOT BE MODIFIED BY THE AGENT - IT IS SOLELY MINE -

After successfully using Claude as my programming teacher for the PCEP exam (passed on Dec 30, 2025), I decided to continue using this strategy and the current goals are:

- to pass the PCAP exam
- to prepare a portfolio project in Python (trades backtesting engine)

I'm planning to achieve both goals by February 28, 2026.

This repository will showcase my learning process, and you can find all the tasks, feedback, exams and separate project parts that I will be working on DAILY.
PLEASE NOTE: WHILE I USE AGENT AS MY TUTOR, I AM NOT USING AI to complete any of the tasks, and the plan is to truly learn and understand all of the concepts on my own, and all of that requires my own work.

As for the commits in this repository, most likely they will be structured and done by the agent, and I will only be pushing them.
As for the agentic flow, while I truly appreciate the current tech advances, I still review all of the proposed changes and accept them manually, so all of the commits etc. will be approved by me and pushed manually.

As for the agent's instructions, I am not planning to publish them as of now, but this might change in the future.

-------------------------------------------

Planned start: 5.01.2026



@20.03 - Roadmap to continue the project:

I've ran the strategy on 216k rows, with a very simple open/close conditions, so no wonder it worked this way hehe.
Test worked properly, I think.

The next steps would be:

1. to implement more sophisticated strategy conditions, maybe add a datetime as one of the conditions of generating a signal.
2. It would also be great to figure out a way to then simulate testing more than one strategy.
3. After we're done with running two strategies (a mini stress-test of the real purpose of this and combining the logic of more than one strategy in the code to still look neat), I have an idea of how we can simulate portfolio performance. We could maybe create a new class for that, or maybe not - that depends.

We could take the datetime and R/profit performance of a given trade, and save it in a df, or wherever.
Then we would do that for every tested strategy, and after every strategy has been tested, we would then take these performance/profit rows with datetimes and sort them by their datetime. We could then simulate portfolio's performance, extract more things like Sharpe/Profit Factor, maybe run Montecarlo simulations etc.

And it all would work without any async and complex logic - just in a kind of a simple way.



Claude's review of my ideas:

Now, your roadmap. Honest take:

Point 1 (datetime conditions) — Good. Filtering signals to RTH session hours only (e.g., 09:00–17:30 CET for FDAX) is exactly how real strategies work. This is the right next step.

Point 2 (multiple strategies simultaneously) — Already architected correctly with current_positions = {strategy: None}. You're one step away — just add a second strategy to the dict and extend the loop. No structural changes needed.

Point 3 (portfolio performance simulation) — The idea is sound and the approach you described is correct. Collect trades with timestamps, sort by datetime, reconstruct cumulative equity curve. This is how backtesting platforms (Backtrader, vectorbt) do it under the hood. The key thing you'd need on each Trade object is an exit_datetime — do you currently store that?

One thing I'd push back on: Sharpe ratio and Monte Carlo before you have a working multi-strategy run is premature. Get two strategies running cleanly, get the equity curve right, then add metrics. Don't over-engineer before the foundation is solid.