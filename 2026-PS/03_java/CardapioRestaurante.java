import java.util.Scanner;

public class CardapioRestaurante {

    public static void main(String[] args) {

        Scanner entrada = new Scanner(System.in);
        int opcao;
        double totalPedido = 0.0; // Variável para acumular o valor total

        // Início do laço de repetição (do-while) para permitir múltiplos itens
        do {
            System.out.println("\n=================================");
            System.out.println("     CARDÁPIO ELETRÔNICO");
            System.out.println("=================================");
            System.out.println("1 - X-Burguer .......... R$ 18,00");
            System.out.println("2 - Pizza .............. R$ 35,00");
            System.out.println("3 - Suco Natural ....... R$  8,00");
            System.out.println("4 - Café ............... R$  5,00");
            System.out.println("0 - Finalizar Pedido");
            System.out.println("=================================");

            System.out.print("Escolha uma opção: ");
            opcao = entrada.nextInt();

            // Estrutura de decisão para processar a escolha e somar os valores
            if (opcao == 1) {
                System.out.println("-> X-Burguer adicionado ao pedido.");
                totalPedido += 18.00;
            } else if (opcao == 2) {
                System.out.println("-> Pizza adicionada ao pedido.");
                totalPedido += 35.00;
            } else if (opcao == 3) {
                System.out.println("-> Suco Natural adicionado ao pedido.");
                totalPedido += 8.00;
            } else if (opcao == 4) {
                System.out.println("-> Café adicionado ao pedido.");
                totalPedido += 5.00;
            } else if (opcao == 0) {
                System.out.println("\nFinalizando o seu pedido...");
            } else {
                System.out.println("Opção inválida! Tente novamente.");
            }

            // Mostra o subtotal parcial a cada item adicionado (opcional)
            if (opcao > 0 && opcao <= 4) {
                System.out.printf("Subtotal atual: R$ %.2f\n", totalPedido);
            }

        } while (opcao != 0); // O loop continua rodando enquanto a opção não for 0

        // Exibição do resumo final da compra
        System.out.println("\n=================================");
        System.out.println("        RESUMO DO PEDIDO");
        System.out.println("=================================");
        System.out.printf("Total a pagar: R$ %.2f\n", totalPedido);
        System.out.println("Obrigado pela preferência e bom apetite!");
        System.out.println("=================================");

        entrada.close();
    }
}