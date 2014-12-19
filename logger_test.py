from logger import Logging

log_path = './logs/logger_test.log'
log_lable = "logger_test"
idc = "BJ"
log = Logging("%s.%s" % (log_path,idc), "%s.%s" % (log_lable,idc))

log.logger.info("info test ok")
log.logger.debug("debug test ok")
log.logger.error("error test ok")
log.logger.warning("warning test ok")
#log.logger.log("log test ok")
log.logger.exception("exception test ok")