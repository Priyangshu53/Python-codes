public class Employee {
    private String name;
    private int eId;
    private double salary;
    private double bonus;

    public Employee(String name, int eId, double salary) {
        this.name = name;
        this.eId = eId;
        this.salary = salary;
        this.bonus = 0.0; // Initialize bonus to zero
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getEId() {
        return eId;
    }

    public void setEId(int eId) {
        this.eId = eId;
    }

    public double getSalary() {
        return salary;
    }

    public void setSalary(double salary) {
        this.salary = salary;
    }

    public double getBonus() {
        return bonus;
    }

    public void setBonus(double bonus) {
        this.bonus = bonus;
    }

    public void calculateBonus(double performanceRating) {
        if (performanceRating >= 1.0 && performanceRating <= 5.0) {
            this.bonus = salary * (performanceRating * 0.1);
        } else {
            System.out.println("Invalid performance rating. Please use a value between 1.0 and 5.0.");
        }
    }

    public static void main(String[] args) {
        Employee employee = new Employee("Priyangshu", 1073, 50000);

        System.out.println("Initial Employee Details:");
        System.out.println("Name: " + employee.getName());
        System.out.println("Employee ID: " + employee.getEId());
        System.out.println("Salary: Rs " + employee.getSalary());
        System.out.println("Bonus: Rs " + employee.getBonus());

        System.out.println("\nCalculating bonus based on performance rating...");
        employee.calculateBonus(4.5);
        System.out.println("Bonus: Rs " + employee.getBonus());
    }
}
