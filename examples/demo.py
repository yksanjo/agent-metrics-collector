#!/usr/bin/env python3
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src import AgentMetricsCollector
def main():
    print("Agent Metrics Collector Demo")
    c = AgentMetricsCollector()
    c.record("a1", "cpu", 50)
    c.record("a1", "cpu", 60)
    print(f"Latest: {c.get_latest('a1', 'cpu')}")
    print("Done!")
if __name__ == "__main__": main()
