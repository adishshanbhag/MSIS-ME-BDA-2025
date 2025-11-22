# Event Slot Booking System for University Convocation (Case-Insensitive Institution Names)

class Institution:
    def __init__(self, name, total_students):
        self.name = name  # Store the original case for printing
        self.total_students = total_students
        self.allowed_per_day = (total_students + 1) // 2  # Ceiling of 50%
        self.booked_per_day = {'Day1': 0, 'Day2': 0, 'Day3': 0}
        self.students = []  # List of (name, reg_number, day) tuples

    def can_book_day(self, day):
        return self.booked_per_day[day] < self.allowed_per_day

    def book_student(self, student_name, reg_number, preferred_day):
        if self.can_book_day(preferred_day):
            self.booked_per_day[preferred_day] += 1
            self.students.append((student_name, reg_number, preferred_day))
            return True
        return False

    def get_students_by_day(self, day):
        return [(name, reg, d) for name, reg, d in self.students if d == day]

class SlotBookingSystem:
    def __init__(self, n_slots_per_day):
        self.n_slots_per_day = n_slots_per_day
        self.total_capacity = n_slots_per_day * 3
        self.institutions = {}  # lowercase name to Institution
        self.allocated_slots = {'Day1': 0, 'Day2': 0, 'Day3': 0}

    def add_institution(self, name, total_students):
        name_key = name.lower()
        if name_key not in self.institutions:
            self.institutions[name_key] = Institution(name, total_students)
            print(f"Institution '{name}' added.")

    def can_book_slot(self, day):
        return self.allocated_slots[day] < self.n_slots_per_day

    def register_student(self, inst_name, student_name, reg_number, preferred_day):
        inst_key = inst_name.lower()
        if inst_key not in self.institutions:
            print("Institution not found.")
            return False, None
        inst = self.institutions[inst_key]
        # Allocate preferred if possible
        for try_day in [preferred_day, 'Day1', 'Day2', 'Day3']:
            if self.can_book_slot(try_day) and inst.can_book_day(try_day):
                if inst.book_student(student_name, reg_number, try_day):
                    self.allocated_slots[try_day] += 1
                    return True, try_day
        # All slots or institution day limits exceeded
        print("No available slots for the institution or on this day.")
        return False, None

    def get_counts_by_institution_day(self):
        result = {}
        for inst_key, inst in self.institutions.items():
            result[inst.name] = dict(inst.booked_per_day)
        return result

    def get_students_for_institution_day(self, inst_name, day):
        inst_key = inst_name.lower()
        if inst_key in self.institutions:
            return self.institutions[inst_key].get_students_by_day(day)
        return []
    
def main():
    n = int(input("Enter total number of slots per day (n): "))
    system = SlotBookingSystem(n)
    while True:
        print("\n--- MENU ---")
        print("1. Institution submits expected student count")
        print("2. Student slot booking")
        print("3. Display count per institution per day")
        print("4. List students of institution for a day")
        print("5. View allocations")
        print("6. Exit")
        choice = input("Choose option: ").strip()
        if choice == '1':
            name = input("Enter institution name: ").strip()
            count = int(input("Enter expected number of students: "))
            system.add_institution(name, count)
        elif choice == '2':
            inst = input("Enter institution name: ").strip()
            stu_name = input("Enter your name: ").strip()
            reg_number = input("Enter your register number: ").strip()
            pref_day = input("Preferred day (Day1/Day2/Day3): ").strip()
            success, day_alloc = system.register_student(inst, stu_name, reg_number, pref_day)
            if success:
                print(f"Slot booked for {day_alloc}.")
            else:
                print("Booking failed.")
        elif choice == '3':
            counts = system.get_counts_by_institution_day()
            for inst in counts:
                print(f"{inst}: {counts[inst]}")
        elif choice == '4':
            inst = input("Enter institution name: ").strip()
            day = input("Enter day (Day1/Day2/Day3): ").strip()
            students = system.get_students_for_institution_day(inst, day)
            print(f"Students from {inst} on {day}:")
            for s in students:
                print(f"  {s[0]} ({s[1]})")
        elif choice == '5':
            print(f"Slots allocated: {system.allocated_slots}")
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == '__main__':
    main()
