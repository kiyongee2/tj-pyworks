class Cart:
    def __init__(self, user_id):
        self.user_id = user_id  #사용자 아이디
        self.items = [] #아이템 저장할 빈 리스트

    # 아이템 추가 메서드
    def add_item(self, item):
        self.items.append(item)
        print(f"아이템 '{item}'이(가) 장바구니에 추가되었습니다.")

    # 아이템 삭제 메서드
    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)
            print(f"아이템 '{item}'이(가) 장바구니에서 제거되었습니다.")
        else:
            print(f"아이템 '{item}'은(는) 장바구니에 없습니다.")

    # 아이템 목로 보기 메서드
    def show_items(self):
        if self.items:
            print("장바구니 아이템 목록:", ", ".join(self.items))
        else:
            print("장바구니가 비어 있습니다.")

# 객체 생성
cart1 = Cart("cloud123")
cart1.add_item("두부")
cart1.add_item("달걀")
cart1.show_items()  #두부, 달걀

# cart1.remove_item("콩나물")
cart1.remove_item("두부")
cart1.show_items()