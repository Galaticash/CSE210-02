

def main():
    person_one = Person()
    person_two = Person()

    person_one.first_name = "Sarah"
    person_two.first_name = "Johnathan"

    person_one.print_name()
    person_two.print_name()


class Person():
    def __init__(self):
        self.first_name = ""
        self.family_name = "Smith"
    def print_name(self):
        print(f"My name is {self.family_name}, {self.first_name}")

if __name__ == "__main__":
    main()
