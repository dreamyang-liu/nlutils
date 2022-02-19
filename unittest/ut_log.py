from nlutils import Logger, PerformanceProfile


with PerformanceProfile("range n"):
    for i in range(1000):
        i += 1

logger = Logger.get_logger()
logger.info("Hello world")
logger.error("Hello world")
logger.debug("Hello world")
logger.warning("Hello world")
logger.fatal("Hello world")


