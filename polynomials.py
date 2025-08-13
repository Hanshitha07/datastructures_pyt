class Node:
    def __init__(self, coefficient, exponent):
        self.coefficient = coefficient
        self.exponent = exponent
        self.next = None

class Polynomial:
    def __init__(self):
        self.head = None
    
    def insert_term(self, coefficient, exponent):
        new_node = Node(coefficient, exponent)
        
        if self.head is None or exponent > self.head.exponent:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next is not None and current.next.exponent >= exponent:
                current = current.next
            new_node.next = current.next
            current.next = new_node
    
    def add_polynomials(self, poly2):
        result = Polynomial()
        p1 = self.head
        p2 = poly2.head
        
        while p1 is not None and p2 is not None:
            if p1.exponent == p2.exponent:
                result.insert_term(p1.coefficient + p2.coefficient, p1.exponent)
                p1 = p1.next
                p2 = p2.next
            elif p1.exponent > p2.exponent:
                result.insert_term(p1.coefficient, p1.exponent)
                p1 = p1.next
            else:
                result.insert_term(p2.coefficient, p2.exponent)
                p2 = p2.next
        
        while p1 is not None:
            result.insert_term(p1.coefficient, p1.exponent)
            p1 = p1.next
            
        while p2 is not None:
            result.insert_term(p2.coefficient, p2.exponent)
            p2 = p2.next
            
        return result
    
    def display(self):
        current = self.head
        terms = []
        while current is not None:
            if current.coefficient != 0:
                sign = "+" if current.coefficient > 0 else ""
                coeff = current.coefficient
                if abs(coeff) == 1 and current.exponent != 0:
                    coeff = "" if coeff == 1 else "-"
                
                if current.exponent == 0:
                    terms.append(f"{sign}{coeff}")
                elif current.exponent == 1:
                    terms.append(f"{sign}{coeff}x")
                else:
                    terms.append(f"{sign}{coeff}x^{current.exponent}")
            current = current.next
        
        poly_str = " ".join(terms)
        if poly_str.startswith("+"):
            poly_str = poly_str[1:]
        return poly_str or "0"

def input_polynomial():
    poly = Polynomial()
    print("\nEnter terms for the polynomial (coefficient exponent).")
    print("Enter 'done' when finished.")
    
    while True:
        term_input = input("Enter term (e.g., '3 2' for 3x^2): ").strip()
        if term_input.lower() == 'done':
            break
        
        try:
            coeff, exp = map(int, term_input.split())
            poly.insert_term(coeff, exp)
        except ValueError:
            print("Invalid input. Please enter two numbers separated by space.")
    
    return poly

def main():
    print("Polynomial Addition Calculator")
    print("=============================")
    
    while True:
        print("\nMENU:")
        print("1. Enter first polynomial")
        print("2. Enter second polynomial")
        print("3. Add polynomials")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ").strip()
        
        if choice == "1":
            print("\nEnter first polynomial:")
            poly1 = input_polynomial()
            print(f"\nFirst polynomial: {poly1.display()}")
        
        elif choice == "2":
            print("\nEnter second polynomial:")
            poly2 = input_polynomial()
            print(f"\nSecond polynomial: {poly2.display()}")
        
        elif choice == "3":
            try:
                if 'poly1' not in locals() or 'poly2' not in locals():
                    print("Please enter both polynomials first!")
                    continue
                
                print("\nPolynomial 1:", poly1.display())
                print("Polynomial 2:", poly2.display())
                
                result = poly1.add_polynomials(poly2)
                print("\nResult of addition:", result.display())
            
            except Exception as e:
                print(f"An error occurred: {e}")
        
        elif choice == "4":
            print("\nThank you for using the Polynomial Calculator!")
            break
        
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()