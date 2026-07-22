import tkinter as tk
# from mss import MSS
# with MSS() as sct:
#     monitor = sct.monitors[1]
#     print(monitor)
#     width = monitor['width']
#     height = monitor['height']
#     monitor = {
#         "top": 0,
#         "left": 0,
#         "width": int(width * 1/3),
#         "height": int(height * 1/2)
    # }
class Overlay(tk.Tk):
    def __init__(self, *a, **kw):
        tk.Tk.__init__(self, *a, **kw)
        self._set_window_attrs()
    
    def _set_window_attrs(self):
        from mss import MSS
        with MSS() as sct:
            monitor = sct.monitors[1]
            # print(monitor)
            width = monitor['width']
            height = monitor['height']
            monitor = {
                "top": 0,
                "left": 0,
                "width": int(width * 1/3),
                "height": int(height * 1/2)
            }
        self.title("Overlay")
        # self.geometry("400x400+100+100")
        self.geometry(f"{int(monitor['width']/3)}x{int(monitor['height']/3)}+{int(monitor['width']/2)}+{int(monitor['height']/5)}")
        # Force window focus
        # self.focus_force()
        self.wm_attributes("-topmost", True)

        # remove borders to prevent resizing
        self.overrideredirect(True)
    
    # def terminate(self):
    #     self.quit()
    
    # btn = tk.Button(self,text='EXIT',command=terminate)

    def run(self):
        self.mainloop()
    
# driver code
if __name__ == "__main__":
    Overlay().run()