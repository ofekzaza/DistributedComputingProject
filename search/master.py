import BaseTypes.master
import _thread
import time

class Master(BaseTypes.master.Master):


    def run(self, state: int = -1):
        """man function of the master"""
        if state == -1:
            state = self.state
        if state == 1:
            self.setMaster()
        if state == 2:
            self.setWorkers()
            time.sleep('3')
        if state == 3:
            if self.haveAnswer():
                return self.answer
        return self.run()

    def haveAnswer(self):
        answer = ""
        for com in self.coms:
            _, _, _, ans, _ = com.recive(self.id)
            answer += str(ans)
        if answer is None:
            return False
        self.answer = answer
        return True