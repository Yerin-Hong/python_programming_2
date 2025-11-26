# 노래 플레이리스트
class Playlist:
    def __init__(self, name):    #  주어진 문제에 '생성자에서 이름 초기화'라고 되어있으니까 init에서는 이름만 초기화.
        self.name = name
        self.tracks = []
    
    def add(self, track):
        self.tracks.append(track)   # 곡 추가

    def count(self):
        return len(self.tracks)     # 곡 개수 반환

    def show(self):
        # 리스트를 문자열로 변환해서 출력 형태 맞춰주기([곡1, 곡2] 이런식으로 출력되어야 함.)
        track_list = ','.join(self.tracks)
        return f"플리명: {self.name}, 곡 수: {self.count()}, 곡들: [{track_list}]"
    
pl = Playlist("MyList")
pl.add("Dynamite"); pl.add("Butter")
print(pl.show())   # 플리명: MyList, 곡 수: 2, 곡들: [Dynamite, Butter]
