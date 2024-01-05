package br.com.comandocerto.playgrounds;

import lombok.extern.slf4j.Slf4j;

@Slf4j
public class SandboxLombokSlf4j {
    
    public void fazerAlgo() {
        log.debug("Mensagem de debug");
        log.info("Mensagem de informação");
        log.warn("Mensagem de aviso");
        log.error("Mensagem de erro");
    }

    public static void main(String[] args) {
        SandboxLombokSlf4j exemplo = new SandboxLombokSlf4j();
        exemplo.fazerAlgo();
    }
}