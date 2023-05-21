import email
import mimetypes
from email.parser import Parser
from org.apache.commons.io import IOUtils
from java.nio.charset import StandardCharsets
from java.io import BufferedReader, InputStreamReader
from org.apache.nifi.processors.script import ExecuteScript
from org.apache.nifi.processor.io import InputStreamCallback
from org.apache.nifi.processor.io import StreamCallback
from datetime import datetime

class PyInputStreamCallback(InputStreamCallback):
    _text = None

    def __init__(self):
        pass

    def getText(self):
        return self._text

    def process(self, inputStream):
        self._text = IOUtils.toString(inputStream, StandardCharsets.UTF_8)
def convertDate(dateString):
    dateObj = datetime.strptime(dateString, "%d-%b-%y")
    year = str(dateObj.year)
    month = str(dateObj.month)
    day = str(dateObj.day)
    return  (year + "-" + month+"-"+ day)

flowFile = session.get()
if flowFile is not None:
    reader = PyInputStreamCallback()
    session.read(flowFile, reader)
    flowFile = session.putAttribute(flowFile, 'msgbody', convertDate("12-Jan-2022"))
    session.transfer(flowFile, ExecuteScript.REL_SUCCESS)