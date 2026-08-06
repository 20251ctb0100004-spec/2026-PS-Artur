import java.util.Scanner;

public class Metodos { 
    
    static double calcularDesconto(double valor, double percentual) {
        double desconto = (percentual / 100) * valor;
        double valorfinal = valor - desconto;
        return valorfinal; 
    }

    static int maiorNumero(int a, int b) {
        if (a > b) {
            return a;
        } else {
            return b; 
        }
    }

    
    static double calcularFrete(double peso) {
        if (peso < 5) {
            return 10.00; // Pesos maiores que 5kg
        } else if (peso < 1) {
            return 20.00; // Pesos entre 1.1kg e 5kg
        } else {
            return 35.00; // Pesos até 1kg (ou valores inválidos/negativos)
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        // --- Método 1: Desconto ---
        System.out.print("Digite o valor do produto: ");
        double valorProduto = scanner.nextDouble();
        
        System.out.print("Digite o percentual de desconto: ");
        double descontoPercentual = scanner.nextDouble();
        
        double resultadoDesconto = calcularDesconto(valorProduto, descontoPercentual);
        System.out.printf("Valor final com desconto: R$ %.2f\n", resultadoDesconto);
        
        System.out.println("-----------------------------------");

        // --- Método 2: Maior Número ---
        System.out.print("Digite o primeiro número inteiro para comparar: ");
        int num1 = scanner.nextInt();
        
        System.out.print("Digite o segundo número inteiro para comparar: ");
        int num2 = scanner.nextInt();

        int maior = maiorNumero(num1, num2);
        System.out.println("O maior número digitado foi: " + maior);
        
        System.out.println("-----------------------------------");

        // --- Método 3: Frete ---
        System.out.print("Digite o peso para calcular o frete: "); 

        double peso = scanner.nextDouble();
        double frete = calcularFrete(peso);
        

        System.out.printf("O valor do frete é: R$ %.2f\n", frete);
        
        scanner.close(); 
    }
}