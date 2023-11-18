public class BankAccount {
    private String accNo;
    private String accHolderName;
    private double balance;

    public BankAccount(String accNo, String accHolderName, double balance) {
        this.accNo = accNo;
        this.accHolderName = accHolderName;
        this.balance = balance;
    }

    public String getAccNo() {
        return accNo;
    }

    public void setAccNo(String accNo) {
        this.accNo = accNo;
    }

    public String getAccHolderName() {
        return accHolderName;
    }

    public void setAccHolderName(String accHolderName) {
        this.accHolderName = accHolderName;
    }

    public double getBalance() {
        return balance;
    }

    public void setBalance(double balance) {
        this.balance = balance;
    }

    public boolean deposit(double amount) {
        if (amount > 0) {
            balance += amount;
            return true;
        } else {
            return false;
        }
    }

    public boolean withdraw(double amount) {
        if (amount > 0 && amount <= balance) {
            balance -= amount;
            return true;
        } else {
            return false;
        }
    }

    public void displayAccountDetails() {
        System.out.println("Account Number: " + accNo);
        System.out.println("Account Holder Name: " + accHolderName);
        System.out.println("Balance: " + balance);
    }

    public static void main(String[] args) {
        BankAccount account = new BankAccount("12345", "John Doe", 1000);

        System.out.println("Initial Account Details:");
        account.displayAccountDetails();

        System.out.println("\nDepositing $500...");
        account.deposit(500);
        account.displayAccountDetails();

        System.out.println("\nWithdrawing $200...");
        account.withdraw(200);
        account.displayAccountDetails();
    }
}
