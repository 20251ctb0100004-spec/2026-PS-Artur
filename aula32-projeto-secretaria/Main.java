/*
- DISCIPLINA: Programação de Sistemas 2026
- ESTUDANTES: Artur Lacerda da Silva
- DATA      : 2026.08.13
- PROJETO   : aula32-projeto-secretaria
- ARQUIVO   : Main.java
*/

// balcao secretaria
import java.util.ArrayList;
import java.util.Scanner;


public class Main {
    public static void main(String[] args) {
        Scanner teclado = new Scanner(System.in);
        // new = carimba uma ficha nova a partir do molde aluno
        // a1 e a2 sao fichas diferentes, cada um cos os seus dados

        // o gaveterio 
        ArrayList<Aluno> lista = new ArrayList<Aluno>();
        
        /* 
        Aluno a1 = new Aluno("Ana Souza", "2026001", "Informatica");
        Aluno a2 = new Aluno("Bia Lima", "2026002", "Mecanica");

        // getNome e getCurso as janelas de leitura de ficha
        a1.setNome("Ana Paula Souza");
        System.out.println(a1.getNome());
        System.out.println(a2.getNome());
        */
        while (true) {
            System.out.println("=====================================");
            System.out.println("          SECRETARIA DO ARTUR         ");
            System.out.println("=====================================");
            System.out.println("[1] Cadastrar Aluno");
            System.out.println("[2] Listar Aluno");
            System.out.println("[3] Buscar por Matricula");
            System.out.println("[4] Atualizar Curso");
            System.out.println("[5] Remover Aluno");
            System.out.println("[0] Sair");
            System.out.print("Sua escolha: ");
            String opcao = teclado.nextLine().trim();

            if (opcao.equals("0")){
                System.out.println("Secreatria Fechada. Ate a proxima neguinho!");
                break;
            } else if (opcao.equals("1")){
                cadastrar (lista, teclado);
            } else if (opcao.equals("2")){
                listar(lista);
            }else if(opcao.equals("3")){
                buscar(lista, teclado);
            }else if(opcao.equals("4")){
                atualizar(lista, teclado);
            }else if(opcao.equals("5")){
                remover(lista, teclado);
            }else{
                System.out.println("Opcao invalida, vale 0, 1, 2, 3, 4 ou 5");
            }

        }
    }
    static void cadastrar(ArrayList<Aluno> lista, Scanner teclado) {
        System.out.print("Nome: ");
        String nome = teclado.nextLine().trim();
        
        System.out.print("Matrícula: ");
        String matricula = teclado.nextLine().trim();

        Aluno existente = buscarPorMatricula(lista, matricula);
        if (existente != null){
            System.out.println("Já existe um aluno com esta matrícula" + matricula);
            return;
        }
        
        System.out.print("Curso: ");
        String curso = teclado.nextLine().trim();

        // Cria a nova ficha
        Aluno novoAluno = new Aluno(nome, matricula, curso);
        
        // Guarda no gaveteiro (ArrayList)
        lista.add(novoAluno);
        System.out.println("--> Aluno cadastrado com sucesso!");
    }

    static void listar(ArrayList<Aluno> lista){
        if (lista.size() == 0){
            System.out.println("Nenuma ficha, adicione novas fichas para listar.");
        }else{
             System.out.println("--- FICHAS NO GAVETERIO ---");
             for (int i = 0; i < lista.size(); i++) {
                Aluno alunoAtual = lista.get(i);
                // Exemplo considerando que os métodos do Aluno sejam getMatricula(), getNome(), getCurso()
                System.out.println(alunoAtual.getMatricula() + " | " + alunoAtual.getNome() + " | " + alunoAtual.getCurso());
            }
        }
    }

    static Aluno buscarPorMatricula(ArrayList<Aluno> lista, String matricula){
        for (int i=0; i < lista.size(); i++){
            Aluno a = lista.get(i);
            if (a.getMatricula().equals(matricula)){
                return a;
            }else{
                System.out.println("Ficha não encontrada");
            }
        } return null;
    }

    static void buscar(ArrayList<Aluno> lista, Scanner teclado){
        System.out.print("Matricula Procurada :");
        String matricula = teclado.nextLine().trim();

        Aluno a = buscarPorMatricula(lista, matricula);

        if (a == null){
            System.out.println("Nenhuma ficha com a matricula " + matricula);
        }else{
            System.out.println("Achei: " + a.getMatricula() + " | " + a.getNome() + " | " + a.getCurso());
        }
    }
 
    static void atualizar(ArrayList<Aluno> lista, Scanner teclado) {        
        System.out.print("Matricula da ficha procurada para atualizar: ");
        String matricula = teclado.nextLine().trim();

        Aluno a = buscarPorMatricula(lista, matricula);     
        if (a == null){
            System.out.println("Nenhuma ficha com a matricula " + matricula);
            return;
        }
        System.out.print("Novo curso de " + a.getNome() + ": ");
        String novoCurso = teclado.nextLine().trim();

        a.setCurso(novoCurso);
        System.out.println("Ficha Atualizada: " + a.getMatricula() + "| " + a.getNome() + " | " + a.getCurso());
    }    

    static void remover(ArrayList<Aluno> lista, Scanner teclado){
        System.out.print("Matricula da ficha para remover: ");
        String matricula = teclado.nextLine().trim();
        Aluno a = buscarPorMatricula(lista, matricula);
        if (a == null){
            System.out.println("Nenhuma ficha com matricula " + matricula);
            return;
        }
        System.out.print("Tem certeza que remove" + a.getNome() + "? (s/n)");
        String resposta = teclado.nextLine().trim();
        if (resposta.equals("s")){
            lista.remove(a);
            System.out.println("Ficha removida");
        }else{
            System.out.println("Remoção Cancelada");
        }
    }
}