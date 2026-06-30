import java.util.ArrayList;

public class Atividade {

    static void main(String[] args) {
        // --- TESTES EXERCÍCIO 1 ---
        System.out.println("--- Exercício 1: Média das Notas ---");
        double[] notas1 = {7.0, 8.0, 9.0};
        System.out.println("Média: " + calcularMedia(notas1)); // Esperado: 8.0
        
        double[] notas2 = {6.0, 6.0, 6.0, 6.0};
        System.out.println("Média: " + calcularMedia(notas2)); // Esperado: 6.0

        // --- TESTES EXERCÍCIO 2 ---
        System.out.println("\n--- Exercício 2: Contador de Aprovados ---");
        double[] notasAprovacao = {7.0, 5.0, 9.0, 6.0};
        System.out.println("Quantidade de Aprovados: " + contarAprovados(notasAprovacao)); // Esperado: 3

        // --- TESTES EXERCÍCIO 3 ---
        System.out.println("\n--- Exercício 3: Catálogo de Produtos ---");
        ArrayList<String> catalogo = new ArrayList<>();
        adicionarProduto(catalogo, "Notebook");
        adicionarProduto(catalogo, "Mouse Gamer");
        adicionarProduto(catalogo, "Teclado Mecânico");
        listarProdutos(catalogo); // Esperado: Lista numerada de 1 a 3

        // --- TESTES EXERCÍCIO 4 ---
        System.out.println("\n--- Exercício 4: Maior Valor (Sobrecarga) ---");
        int[] inteiros = {3, 9, 5};
        System.out.println("Maior inteiro: " + maiorValor(inteiros)); // Esperado: 9

        double[] decimais = {1.5, 4.8, 2.2};
        System.out.println("Maior decimal: " + maiorValor(decimais));

        // --- TESTES EXERCÍCIO 5 ---
        System.out.println("\n--- Exercício 5: Boletim Integrador ---");
        double[] notasBoletim1 = {7.0, 5.0, 9.0, 6.0};
        exibirBoletim(notasBoletim1); // Esperado: Média 6.75, 3 aprovados, APROVADA
        
        System.out.println();
        double[] notasBoletim2 = {4.0, 3.0, 5.0};
        exibirBoletim(notasBoletim2); // Esperado: Média 4.0, 0 aprovados, EM RECUPERAÇÃO
    }

    // 1
    static double calcularMedia(double[] notas) {
        if (notas == null || notas.length == 0) {
            return 0.0;
        }
        double soma = 0.0;
        for (double nota : notas) {
            soma += nota;
        }
        return soma / notas.length;
    }

    // 2
    static int contarAprovados(double[] notas) {
        if (notas == null) {
            return 0;
        }
        int aprovados = 0;
        for (double nota : notas) {
            if (nota >= 6.0) { // Critério padrão de aprovação (nota maior ou igual a 6.0)
                aprovados++;
            }
        }
        return aprovados;
    }

    // 3
    static void adicionarProduto(ArrayList<String> lista, String nome) {
        if (lista != null && nome != null && !nome.trim().isEmpty()) {
            lista.add(nome);
        }
    }
    // 4
    static void listarProdutos(ArrayList<String> lista) {
        if (lista == null || lista.isEmpty()) {
            System.out.println("O catálogo está vazio.");
            return;
        }
        for (int i = 0; i < lista.size(); i++) {
            System.out.println((i + 1) + ". " + lista.get(i));
        }
    }
    // 5
    static int maiorValor(int[] array) {
        if (array == null || array.length == 0) {
            throw new IllegalArgumentException("O array não pode ser vazio ou nulo.");
        }
        int maior = array[0];
        for (int valor : array) {
            if (valor > maior) {
                maior = valor;
            }
        }
        return maior;
    }

    // Sobrecarga do método maiorValor para aceitar números decimais (double) 5
    static double maiorValor(double[] array) {
        if (array == null || array.length == 0) {
            throw new IllegalArgumentException("O array não pode ser vazio ou nulo.");
        }
        double maior = array[0];
        for (double valor : array) {
            if (valor > maior) {
                maior = valor;
            }
        }
        return maior;
    }
    // 6
    static void exibirBoletim(double[] notas) {
        double media = calcularMedia(notas);
        int aprovados = contarAprovados(notas);
        String situacao;

        // Regra de negócio para a situação com base na média obtida
        if (media >= 6.0) {
            situacao = "APROVADA";
        } else {
            situacao = "EM RECUPERAÇÃO";
        }

        System.out.println("Média: " + media);
        System.out.println("Aprovados: " + aprovados);
        System.out.println("Situação: " + situacao);
    }
}