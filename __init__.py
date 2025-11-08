"""
Logger Module - A comprehensive logging utility for experiment tracking
"""

from .Logger import LoggerFormatter

__version__ = "1.0.0"
__author__ = "EDTAwhy"
__all__ = ["LoggerFormatter"]

# Module docstring
"""
LoggerFormatter is a comprehensive logging utility designed for experiment tracking and data management.

Main features:
- Automatic timestamped directory creation
- Hyperparameter saving (auto-detects UPPERCASE variables)
- High-quality figure export
- Large variable storage with pickle
- Source code backup
- Random seed management

Quick start:
    from Logger import LoggerFormatter
    
    logger = LoggerFormatter(project_name="my_experiment")
    logger.seed_everything(42)
    logger.save_hyperparameters()
"""
