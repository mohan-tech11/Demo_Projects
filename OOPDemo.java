// Interface: defines behavior that implementing classes must provide.
interface Payable {
    double calculatePay();
}

// Abstract class: cannot be instantiated directly.
abstract class Employee implements Payable {
    // Encapsulation: fields are private and accessed through methods.
    private String name;
    private double baseSalary;

    public Employee(String name, double baseSalary) {
        this.name = name;
        this.baseSalary = baseSalary;
    }

    public String getName() {
        return name;
    }

    public double getBaseSalary() {
        return baseSalary;
    }

    // Abstract method: subclasses must implement it.
    public abstract String getRole();

    public void displayDetails() {
        System.out.println(
            getRole() + ": " + name +
            ", Pay: $" + calculatePay()
        );
    }
}

// Inheritance: Manager is a kind of Employee.
class Manager extends Employee {
    private double bonus;

    public Manager(String name, double baseSalary, double bonus) {
        super(name, baseSalary);
        this.bonus = bonus;
    }

    // Polymorphism: Manager provides its own implementation.
    @Override
    public double calculatePay() {
        return getBaseSalary() + bonus;
    }

    @Override
    public String getRole() {
        return "Manager";
    }
}

class Developer extends Employee {
    private int overtimeHours;
    private double hourlyRate;

    public Developer(
        String name,
        double baseSalary,
        int overtimeHours,
        double hourlyRate
    ) {
        super(name, baseSalary);
        this.overtimeHours = overtimeHours;
        this.hourlyRate = hourlyRate;
    }

    @Override
    public double calculatePay() {
        return getBaseSalary() + overtimeHours * hourlyRate;
    }

    @Override
    public String getRole() {
        return "Developer";
    }
}

// Composition: a Company "has" employees.
class Company {
    private Employee[] employees;

    public Company(Employee[] employees) {
        this.employees = employees;
    }

    public void printPayroll() {
        for (Employee employee : employees) {
            employee.displayDetails();
        }
    }
}

public class OOPDemo {
    public static void main(String[] args) {
        Employee[] employees = {
            new Manager("Asha", 70000, 10000),
            new Developer("Ravi", 60000, 10, 500)
        };

        Company company = new Company(employees);
        company.printPayroll();
    }
}