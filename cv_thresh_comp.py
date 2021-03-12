import cv2
import numpy as np
import matplotlib.pyplot as plt

class CVThreshComp():
    def __init__(self, image, titles, types):
        self.org = image
        self.img = image.copy()
        self.titles = titles
        self.types = types
        self.val = 0
        self.typ = (types[0], titles[0])
        
    def preview(self):
        cv2.namedWindow('preview', cv2.WINDOW_AUTOSIZE)
        cv2.moveWindow('preview', 0, 0)
        key = 0
        idx = 0
        while key != ord('q'):
            org = cv2.putText(self.org.copy(), f"ORIGINAL", (100,100), cv2.FONT_HERSHEY_SIMPLEX ,  
                           2, [255,255,255], 6, cv2.LINE_AA) 
            org = cv2.putText(org, f"ORIGINAL", (100,100), cv2.FONT_HERSHEY_SIMPLEX ,  
                           2, [0,0,255], 2, cv2.LINE_AA) 

            cv2.imshow('preview', org)
            key = cv2.waitKey(1000)
            while key != ord('q'):
                key = cv2.waitKey(10)
                info = [str(self.val), self.typ[1]]
                self.val += 1
                if self.val == 255:
                    break
                _, thresh_img = cv2.threshold(self.img, self.val, 255, self.typ[0])
                thresh_img = cv2.putText(thresh_img, f"{info[0]} : {info[1]}", (100,100), cv2.FONT_HERSHEY_SIMPLEX ,  
                                           2, [255,255,255], 6, cv2.LINE_AA) 
                thresh_img = cv2.putText(thresh_img, f"{info[0]} : {info[1]}", (100,100), cv2.FONT_HERSHEY_SIMPLEX ,  
                                           2, [0,0,255], 2, cv2.LINE_AA)
                cv2.imshow('preview', thresh_img)

            self.val = 0
            if idx == 4:
                break
            idx += 1
            self.typ = (self.types[idx], self.titles[idx])
        cv2.destroyAllWindows()
        cv2.waitKey(1)
            
    def tracker(self):
        cv2.namedWindow('preview', cv2.WINDOW_AUTOSIZE)
        cv2.moveWindow('preview', 0, 0)
        cv2.createTrackbar("Value", 'preview', 0, 255, self._track_action)
        cv2.createTrackbar("Type", 'preview', 0, len(self.types)-1, self._track_action_gate)
        cv2.imshow('preview', self.org)
        while True:
            key = cv2.waitKey()
            if key == ord('q'):
                cv2.destroyAllWindows()
                cv2.waitKey(1)
                break
        

    def _track_action(self, val):
        self.val = val
        info = [str(self.val), self.typ[1]]
        _, thresh_img = cv2.threshold(self.img, self.val, 255, self.typ[0])
        thresh_img = cv2.putText(thresh_img, f"{info[0]} : {info[1]}", (100,100), cv2.FONT_HERSHEY_SIMPLEX ,  
                                   2, [255,255,255], 6, cv2.LINE_AA) 
        thresh_img = cv2.putText(thresh_img, f"{info[0]} : {info[1]}", (100,100), cv2.FONT_HERSHEY_SIMPLEX ,  
                                   2, [0,0,255], 2, cv2.LINE_AA)
        cv2.imshow('preview', thresh_img)

    def _track_action_gate(self, val):
        self.typ = (self.types[val], self.titles[val])
        self._track_action(self.val)
