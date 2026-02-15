"""Agent Metrics Collector - Metrics collection for agent systems."""

from typing import Dict, List, Any
from dataclasses import dataclass, field
from datetime import datetime
import uuid

@dataclass
class Metric:
    name: str
    value: float
    timestamp: datetime = field(default_factory=datetime.now)

class AgentMetricsCollector:
    def __init__(self):
        self.metrics: Dict[str, List[Metric]] = {}
    
    def record(self, agent_id: str, metric_name: str, value: float) -> None:
        if agent_id not in self.metrics:
            self.metrics[agent_id] = []
        self.metrics[agent_id].append(Metric(name=metric_name, value=value))
    
    def get_metrics(self, agent_id: str) -> List[Metric]:
        return self.metrics.get(agent_id, [])
    
    def get_latest(self, agent_id: str, metric_name: str) -> float:
        agent_metrics = self.metrics.get(agent_id, [])
        for m in reversed(agent_metrics):
            if m.name == metric_name:
                return m.value
        return 0.0

__all__ = ["AgentMetricsCollector", "Metric"]
