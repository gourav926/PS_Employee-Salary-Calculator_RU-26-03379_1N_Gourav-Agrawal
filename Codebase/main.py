
# PS No. 96 - Employee Salary Calculator
# Language : Python 3
# Concepts : Functions, Operators, Conditions

# Rates given in the problem (easy to change here)
HRA_RATE = 0.20   # HRA = 20% of basic
DA_RATE = 0.10    # DA  = 10% of basic
PF_RATE = 0.12    # PF  = 12% of basic
# Small helper: shows 6000.0 as 6000, but keeps 1950.5 as 1950.50
def show(number):
    if number == int(number):
        return str(int(number))
    return "{:.2f}".format(number)

# Function 1: get a valid salary from the user
# Keeps asking until the user types a positive number
def get_salary():
    while True:
        text = input("Enter basic salary: ")
        try:
            salary = float(text)      # try to convert text to a number
        except ValueError:            # happens when user types "abc"
            print("Invalid salary. Enter a positive number.")
            continue                  # go back and ask again

        if salary <= 0:               # negative or zero is not allowed
            print("Invalid salary. Enter a positive number.")
        else:
            return salary             # get salary, send it back

# Function 2: calculate HRA, DA and Gross salary
# Gross = Basic + HRA + DA

def calculate_gross(basic):
    hra = basic * HRA_RATE
    da = basic * DA_RATE
    gross = basic + hra + da
    return hra, da, gross

# Function 3: calculate PF (12% of basic)
def calculate_pf(basic):
    return basic * PF_RATE

# Function 4: calculate tax on GROSS salary using conditions
#   up to 25000        -> no tax
#   25001 to 50000     -> 5%
#   above 50000        -> 10%
def calculate_tax(gross):
    if gross <= 25000:
        tax = 0
    elif gross <= 50000:
        tax = gross * 0.05
    else:
        tax = gross * 0.10
    return tax

# Function 5: print the salary slip
def print_slip(name, emp_id, basic, hra, da, gross, pf, tax, net):
    print()
    print("=" * 36)
    print("          SALARY SLIP")
    print("=" * 36)
    print("Employee Name :", name)
    print("Employee ID   :", emp_id)
    print("-" * 36)
    print("Basic Salary  :", show(basic))
    print("HRA (20%)     :", show(hra))
    print("DA (10%)      :", show(da))
    print("Gross Salary  :", show(gross))
    print("-" * 36)
    print("PF (12%)      :", show(pf))
    print("Tax           :", show(tax))
    print("-" * 36)
    print("NET SALARY    :", show(net))
    print("=" * 36)

    # The same lines in the format asked in the test cases
    print("HRA:", show(hra), "| DA:", show(da), "| Gross:", show(gross))
    print("PF:", show(pf), "| Tax:", show(tax), "| Net Salary:", show(net))

# EXTRA FEATURE: save the slip into a text file
def save_slip(name, emp_id, basic, hra, da, gross, pf, tax, net):
    file = open("salary_slips.txt", "a")      # "a" = add at the end of file
    file.write("Name: " + name + " | ID: " + emp_id + "\n")
    file.write("Basic: " + show(basic) + "\n")
    file.write("HRA: " + show(hra) + " | DA: " + show(da) +
               " | Gross: " + show(gross) + "\n")
    file.write("PF: " + show(pf) + " | Tax: " + show(tax) +
               " | Net Salary: " + show(net) + "\n")
    file.write("-" * 36 + "\n")
    file.close()
# MAIN PROGRAM
def main():
    print("===== EMPLOYEE SALARY CALCULATOR =====")

    # EXTRA FEATURE: lists to remember every employee we process
    all_names = []
    all_net_salaries = []

    # Loop: keep going while the user says yes
    while True:
        print()
        name = input("Enter employee name: ")
        emp_id = input("Enter employee ID: ")
        basic = get_salary()

        # Do all the calculations by calling our functions
        hra, da, gross = calculate_gross(basic)
        pf = calculate_pf(basic)
        tax = calculate_tax(gross)
        net = gross - pf - tax            # Net = Gross - PF - Tax

        print_slip(name, emp_id, basic, hra, da, gross, pf, tax, net)
        save_slip(name, emp_id, basic, hra, da, gross, pf, tax, net)
        print("Slip saved to salary_slips.txt")

        # Remember this employee for the final summary
        all_names.append(name)
        all_net_salaries.append(net)

        more = input("\nAdd another employee? (yes/no): ").lower()
        if more != "yes" and more != "y":
            break             
          # stop the loop
    # EXTRA FEATURE: summary of the whole session
    print()
    print("=" * 36)
    print("          SUMMARY")
    print("=" * 36)
    print("Employees processed :", len(all_names))
    print("Total salary payout :", show(sum(all_net_salaries)))

    highest = max(all_net_salaries)
    position = all_net_salaries.index(highest)
    print("Highest paid        :", all_names[position], "-", show(highest))
    print("Thank you!")
# Python starts running from here
main()
