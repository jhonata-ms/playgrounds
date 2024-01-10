package br.com.comandocerto.playgrounds;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.util.Scanner;

public class SandboxFile {
    public static void main(String[] args) {
        //SandboxFile.lerArquivo();
        SandboxFile.listarArquivos();
    }

    public static void lerArquivo() {
        String caminhoArquivo = "./README.md";

        try (BufferedReader br = new BufferedReader(new FileReader(caminhoArquivo))) {
            StringBuilder conteudo = new StringBuilder();
            String linha;

            while ((linha = br.readLine()) != null) {
                conteudo.append(linha).append("\n");
            }

            String conteudoDoArquivo = conteudo.toString();
            System.out.println("Conteúdo do arquivo:\n" + conteudoDoArquivo);

        } catch (IOException e) {
            e.printStackTrace();
        }
    }
    public static void listarArquivos() {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Informe o caminho do diretório:");
        String caminhoDiretorio = scanner.nextLine();

        System.out.println("Deseja listar apenas o primeiro nível? (S/N):");
        char opcao = scanner.nextLine().toUpperCase().charAt(0);

        File diretorio = new File(caminhoDiretorio);

        // Verifica se o caminho representa um diretório válido
        if (diretorio.isDirectory()) {
            if (opcao == 'S') {
                // Listar apenas o primeiro nível
                listarPrimeiroNivel(diretorio);
            } else {
                // Listar todos os níveis
                exibirConteudo(diretorio, 0);
            }
        } else {
            System.out.println("Caminho especificado não é um diretório válido.");
        }

        scanner.close();
    }
    private static void listarPrimeiroNivel(File diretorio) {
        File[] itens = diretorio.listFiles();

        if (itens != null) {
            System.out.println("Conteúdo do diretório (primeiro nível):");

            for (File item : itens) {
                if (item.isDirectory()) {
                    System.out.println("Diretório: " + item.getName());
                } else {
                    System.out.println("Arquivo: " + item.getName());
                }
            }
        } else {
            System.out.println("O diretório está vazio.");
        }
    }

    private static void exibirConteudo(File item, int nivel) {
        if (item.isDirectory()) {
            // Imprime o nome do diretório
            imprimirIndentacao(nivel);
            System.out.println("Diretório: " + item.getName());

            // Lista e exibe o conteúdo da subpasta
            File[] subItens = item.listFiles();
            if (subItens != null) {
                for (File subItem : subItens) {
                    exibirConteudo(subItem, nivel + 1);
                }
            }
        } else {
            // Imprime o nome do arquivo
            imprimirIndentacao(nivel);
            System.out.println("Arquivo: " + item.getName());
        }
    }

    private static void imprimirIndentacao(int nivel) {
        for (int i = 0; i < nivel; i++) {
            System.out.print("  "); // Duas espaços por nível
        }
    }
}
