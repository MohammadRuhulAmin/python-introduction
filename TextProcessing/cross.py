from org.apache.commons.io import IOUtils
from java.nio.charset import StandardCharsets

flowfile = session.get()
if flowfile is not None:
    flowfile_content = ""
    try:
        inputStream = session.read(flowfile)
        flowfile_content = IOUtils.toString(inputStream, StandardCharsets.UTF_8)
    except Exception as e:
        log.error("Failed to read content of flowfile {}: {}".format(flowfile.getAttribute('uuid'), str(e)))
        session.transfer(flowfile, REL_FAILURE)
        raise e
    finally:
        inputStream.close()

    if flowfile_content != "":
        log.info("Content of flowfile {}: {}".format(flowfile.getAttribute('uuid'), flowfile_content))
        session.transfer(flowfile, REL_SUCCESS)
    else:
        log.error("Content of flowfile {} is empty".format(flowfile.getAttribute('uuid')))
        session.transfer(flowfile, REL_FAILURE)
