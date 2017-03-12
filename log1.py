import logging
logging.basicConfig(filename="log1.txt",format="%(asctime)s->%(levelname)s->%(message)s", level=logging.INFO)
logging.info("....info statement...")
logging.debug("debug statement")
logging.warn("warning statement")
logging.error("Error statement")
logging.exception("Exception statement")