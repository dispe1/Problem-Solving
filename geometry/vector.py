import math
import sys

class vector2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return vector2(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return vector2(self.x - other.x, self.y - other.y)

    def __mul__(self, int):
        return vector2(self.x * int, self.y * int)

    def __truediv__(self, int):
        return vector2(self.x / int, self.y / int)

    def __str__(self):
        return str(self.x) + ' ' + str(self.y)

    def __cmp__(self, other):
        temp = self - other
        if temp.x == 0:
            if temp.y == 0:
                return 0
            elif temp.y > 0:
                return 1
            else:
                return -1
        elif temp.x > 0:
            return 1
        else:
            return -1

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __lt__(self, other):
        return self.__cmp__(other) < 0

    def __le__(self, other):
        return self.__cmp__(other) <= 0

    def __gt__(self, other):
        return self.__cmp__(other) > 0

    def __ge__(self, other):
        return self.__cmp__(other) >= 0
    #벡터의 길이를 반환한다.
    def norm(self):
        return math.sqrt(self.x * self.x + self.y * self.y)
    #방향이 같은 단위 벡터(unit vector)를 반환한다.
    def normalize(self):
        return vector2(self.x / self.norm(), self.y / self.norm()) if self.norm() != 0 else vector2(0, 0)
    #x축의 양의 방향으로부터 이 벡터까지 반시계 방향으로 잰 각도
    #[-pi, pi] -> [0, 2 * pi) 보정 | radian * 180 / math.pi -> degree
    def polar(self):
        return math.fmod(math.atan2(self.y, self.x) + 2 * math.pi, 2*math.pi)
    #내적 | 0이면 직각(pi / 2 or 3*pi / 2)
    def dot(self, other):
        return self.x * other.x + self.y * other.y
    #외적 | 외적의 절대값 = self, other을 두 변으로 하는 평행 사변형의 넓이
    #외적이 양수라면 other이 self로 부터 반시계 방향으로 180도 이내
    #외적이 음수라면 other이 self로 부터 시계 방향으로 180도 이내
    def cross(self, other):
        return self.x * other.y - other.x * self.y
    #벡터의 사이각
    def angle(self, other):
        return math.acos(self.dot(other) / (self.norm() * other.norm()) )
    #self를 other에 사영한 결과
    def project(self, other):
        r = other.normalize()
        return r * r.dot(self)

#원점에서 벡터 b가 벡터 a의 반시계 방향이면 양수, 시계 방향이면 음수, 평행이면 0을 반환
def ccw(a, b):
    return a.cross(b)
#점 p를 기준으로 벡터 b가 a의 반시계 방향이면 양수, 시계 방향이면 음수, 평행이면 0을 반환
def ccw2(p, a, b):
    return ccw(a-p, b-p)

#(a,b)를 포함하는 직선과 (c,d)를 포함하는 직선의 교점을 x에 반환한다.
#두 직선이 평행이면 (겹치는 경우를 포함) 거짓을, 아니면 참을 반환한다.
def lineIntersection(a, b, c, d, x):
    det = (b - a).cross(d - c)
    #두 직선이 평행인 경우
    if math.fabs(det) < sys.float_info.epsilon: return False
    x = a + (b - a) * ((c - a).cross(d - c) / det)
    return True

#(a,b)와 (c, d)가 평행한 두 선분일 때 이들이 한 점에서 겹치는지 확인한다.
def parrallelSegments(a, b, c, d, p):
    if b < a: a, b = b, a
    if d < c: c, d = d, c
    #한 직선 위에 없거나 두 선분이 겹치지 않는 경우를 우선 걸러낸다.
    if ccw2(a, b, c) != 0 or b < c or d < a: return False
    #두 선분은 확실히 겹친다. 교차점을 하나 찾자.
    p = c if a < c else a
    return True

#p가 (a,b)를 감싸면서 각 변이 x, y축에 평행한 최소 사각형 내부에 있는지 확인한다.
#a, b, p는 일직선 상에 있다고 가정한다.
def inBoundingRectangle(p, a, b):
    if b < a: a, b = b, a
    return p == a or p == b or (a < p and p < b)

#(a, b) 선분과 (c, d) 선분의 교점을 p에 반환한다.
#교점이 여러 개일 경우 아무 점이나 반환한다.
#두 선분이 교차하지 않을 경우 False를 반환한다.
def segmentIntersection(a, b, c, d, p):
    #두 직선이 평행인 경우를 우선 예외처리한다.
    if not lineIntersection(a, b, c, d, p):
        return parrallelSegments(a, b, c, d, p)
    #p가 두 선분에 포함되어 있는 경우에만 참을 반환한다.
    return inBoundingRectangle(p, a, b) and inBoundingRectangle(p, c, d)

#두 선분이 서로 접촉하는지 여부를 반환한다.
def segmentIntersects(a, b, c, d):
    ab = ccw2(a, b, c) * ccw2(a, b, d)
    cd = ccw2(c, d, a) * ccw2(c, d, b)
    #두 선분이 한 직선 위에 있거나 끝점이 겹치는 경우
    if ab == 0 and cd == 0:
        if b < a: a, b = b, a
        if d < c: c, d = d, c
        return not (b < c or d < a)
    return ab <= 0 and cd <= 0

#점 p에서 (a, b) 직선에 내린 수선의 발을 구한다.
def perpendicularFoot(p, a, b):
    return a + (p - a).project(b - a)
#점 p와 (a,b) 직선 사이의 거리를 구한다.
def pointToLine(p, a, b):
    return (p - perpendicularFoot(p, a, b)).norm()

#주어진 단순 다각형 p의 넓이를 구한다.
#p는 각 꼭지점의 취지 벡터의 집합으로 주어진다.
def area(p):
    ret = 0
    for i in range(len(p)):
        j = (i + 1) % len(p)
        ret += p[i].x * p[j].y - p[j].x * p[i].y

    return math.fabs(ret) / 2

#점 q가 다각형 p 안에 포함되어 있을 경우 참, 아닌 경우 거짓을 반환한다.
#q가 다각형의 경계 위에 있는 경우의 반환 값은 정의되어 있지 않다.
def isInside(q, p):
    crosses = 0
    for i in range(len(p)):
        j = (i + 1) % len(p)
        #(p[i], p[j])가 반직선을 세로로 가로지르는가?
        if (p[i].y > q.y) != (p[j].y > q.y):
            #가로지르는 x 좌표를 계산한다.
            atX = (p[j].x - p[i].x) * (q.y - p[i].y) / (p[j].y - p[i].y) + p[i].x
            if q.x < atX:
                crosses += 1

    return crosses % 2 == 1


# a = vector2(1,2)
# b = vector2(1,1)
# c = vector2(2,1)
# d = vector2(1.5, 1.3)
# print(area([a,b,c]))
# print(isInside(d, [a, b, c]))
# print(a == b)
# print(a > b)
# print(a.norm())
# print(a.normalize())
# print(b.polar() * 180 / math.pi)
# print(a.dot(b))
# print(a.cross(b))
# print(a.project(b))
# print(a.angle(b) * 180 / math.pi)
# print(ccw2(vector2(1,1), vector2(1,2), vector2(2,1)))
