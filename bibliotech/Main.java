/*
 * Disciplina: 2026-PS
 * Projeto   : bibliotech
 * Arquivo   : Main.java
 * Descricao : Classe principal para testar o funcionamento da classe Livro.
 */
public class Main {

    public static void main(String[] args) {
        // Criacao de instancias (objetos) da classe Livro
        Livro livro1 = new Livro("O Senhor dos Aneis", "J.R.R. Tolkien", 1954);
        Livro livro2 = new Livro("Dom Casmurro", "Machado de Assis", 1899);

        // Exibicao do estado inicial dos livros
        System.out.println("--- Estado Inicial ---");
        System.out.println(livro1.toString());
        System.out.println(livro2.toString());

        // Simulando o emprestimo do primeiro livro
        System.out.println("\n--- Emprestando o livro 1 ---");
        livro1.emprestar();
        System.out.println(livro1.toString());

        // Verificando a disponibilidade
        System.out.println("O livro 1 esta disponivel? " + livro1.estaDisponivel());
        System.out.println("O livro 2 esta disponivel? " + livro2.estaDisponivel());

        // Simulando a devolucao do primeiro livro
        System.out.println("\n--- Devolvendo o livro 1 ---");
        livro1.devolver();
        System.out.println(livro1.toString());
    }
}