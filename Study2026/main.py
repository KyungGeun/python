class Student:
    def __init__(self, name, scores, number, classNumber):
        self.name = name
        self.scores = scores
        self.number = number
        self.classNumber = classNumber
        self.average = 0
        self.scoresLen = len(scores)

    def inputScore(self):
        for i in range(self.scoresLen):
            score = 0
            print(f"{self.scores[i][0]}의 점수를 입력하세요.", end=" ")
            score = int(input())
            self.scores[i][1] = score

    def updateSubjectScore(self):
        print("수정하고 싶은 학생의 과목을 입력하세요.")
        print("(국어 : 1, 수학 : 2, 영어 : 3, 과학 : 4, 역사 : 5)", end= " ")
        number = int(input())

        print("점수를 입력하세요.", end= " ")
        score = int(input())

        self.scores[number - 1][1] = score

    def calculateAverage(self):
        total = 0

        for i in range(self.scoresLen):
            total += self.scores[i][1]

        self.average = total / self.scoresLen

    def maxScoreFind(self):
        self.maxScore = -1

        for i in range(self.scoresLen):
            if (self.maxScore < self.scores[i][1]) : self.maxScore = self.scores[i][1]

    def minScoreFind(self):
        self.minScore = -1

        for i in range(self.scoresLen):
            if (self.minScore > self.scores[i][1]) : self.minScore = self.scores[i][1]

    def printStudentInfo(self):
        print()
        print(f"[{self.name} 학생]", end=" ")
        print()

        for i in range(self.scoresLen):
            print(f"{self.scores[i][0]} 점수는", end= " ")
            print(f"{self.scores[i][1]}입니다.")

        for i in range(self.scoresLen):
            if (self.scores[i][1] == self.minScore):
                print(f"제일 못 본 과목은 {self.minScore}점으로", end= " ")
                print(f"{self.scores[i][0]}입니다.")
                break

        for i in range(self.scoresLen):
            if (self.scores[i][1] == self.maxScore):
                print(f"제일 잘 본 과목은 {self.maxScore}점으로", end= " ")
                print(f"{self.scores[i][0]}입니다.")
                break

        print(f"평균 점수는 : {self.average}입니다.")

scores = [["국어", 50], ["수학", 85], ["영어", 20], ["과학", 75], ["역사", 15]]

print(f"[현재 scores]\n{scores}\n")

OKG = Student("OKG", scores, 5, 5)
OKG.updateSubjectScore()
OKG.updateSubjectScore()
OKG.calculateAverage()
OKG.maxScoreFind()
OKG.minScoreFind()
OKG.printStudentInfo()