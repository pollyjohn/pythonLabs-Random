class Camera:
    def __init__(self, name, taking_photo = False, recording = True ) -> None:
        self.name =  name
        self.recording =  recording
        self.taking_photo =  taking_photo

    def record(self):
        if self.taking_photo:
            print(f"{self.name} is taking_photo. Can't record.")
        elif self.recording == True:
            print(f"{self.name} is already recording")
            return
        self.recording = True
        print(f'{self.name} is recording')

    def stop_recording(self):
        if self.recording != True:
            print(f"{self.name} is not recording")
            return
        self.recording = False
        print(f"{self.name} stopped recording")

    def take_photo(self):
        if self.recording:
            print(f"{self.name} is already recording. can't take photo")
            return
        self.taking_photo == True
        print(f'{self.name} took photo')

c1 = Camera('canon')
c1.record()
c1.record()
c1.take_photo()
c1.stop_recording()
c1.take_photo()

c2 = Camera('panasonic')
c2.take_photo()
c2.record()
c2.stop_recording()
c2.stop_recording()
c2.take_photo()
