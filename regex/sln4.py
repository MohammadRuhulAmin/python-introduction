import re
import json
import uuid
from datetime import datetime
import email
import mimetypes
from email.parser import Parser
from org.apache.commons.io import IOUtils
from java.nio.charset import StandardCharsets
from java.io import BufferedReader, InputStreamReader
from org.apache.nifi.processors.script import ExecuteScript
from org.apache.nifi.processor.io import InputStreamCallback
from org.apache.nifi.processor.io import StreamCallback
from org.apache.nifi.processor.io import OutputStreamCallback


class PyInputStreamCallback(InputStreamCallback):
    _text = None
    def __init__(self):
        pass

    def getText(self):
        return self._text

    def process(self, inputStream):
        self._text = IOUtils.toString(inputStream, StandardCharsets.UTF_8)
class PyOutputStreamCallback(OutputStreamCallback):
    def __init__(self, data):
        self.data = data

    def process(self, outputStream):
        outputStream.write(bytearray(self.data.encode('utf-8')))



flowFile = session.get()

def convertDate(dateString):
    dateObj = datetime.strptime(dateString, "%d-%b-%y")
    year = str(dateObj.year)
    month = str(dateObj.month)
    day = str(dateObj.day)
    return (year + "-" + month + "-" + day)

def convertDate(dateString):
    dateObj = datetime.strptime(dateString, "%d-%b-%y")
    year = str(dateObj.year)
    month = str(dateObj.month)
    day = str(dateObj.day)
    return  (year + "-" + month+"-"+ day)
def process_data():

    #Flight_Date = flowFile.getAttribute('Flight_Date')
    Flight_Date = "12-Jun-2022"
    processedFlightDate = convertDate(Flight_Date)
    return processedFlightDate



    flowFile = session.putAttribute(flowFile, 'formated_flight_date', "Goodjob")
    session.transfer(flowFile, ExecuteScript.REL_SUCCESS)
