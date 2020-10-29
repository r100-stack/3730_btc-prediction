import sys

class Util():
    __instance = None

    def __init__(self, _debug, _print):
        if Util.__instance == None:
            Util.__instance = self
            self._errorFlag = _debug
            self._printFlag = _print
        else:
            self._error("Util is a singleton class. Please use getInstance().")

    @staticmethod
    def getInstance():
        if Util.__instance == None:
            return Util(False, False)
        else:
            return Util.__instance

    #prints received _header and _msg to stdout, with optional newline and separator at beginning and end
    def outPrt(self, _header="Output:", _msg="", _newline=True, _separator=False):
        #if we don't want to print, return
        if not self._printFlag:
            return
        #otherwise print stuff
        if _newline:
            sys.stdout.write("\n")
        if _separator:
            sys.stdout.write("-------------------------")

        #print _header and _msg
        sys.stdout.write(f"{_header}\n")
        sys.stdout.write(f"{_msg}")

        if _separator:
            sys.stdout.write("-------------------------")
        if _newline:
            sys.stdout.write("\n")
        sys.stdout.flush()

    #prints received error to stderr
    def errPrt(self, _msg):
        #if we don't want to print, return
        if not self._errorFlag:
            return

        #print _msg
        sys.stderr.write("Error:  " + _msg + "\n")
        sys.stderr.flush()