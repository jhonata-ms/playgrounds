package br.com.comandocerto.playgrounds;

import reactor.core.publisher.Flux;

public class SandboxReactor {
    public static void main(String[] args) {
        Flux<Integer> flux = Flux.just(1, 2, 3, 4, 5);

        flux.subscribe(System.out::println);

        flux
            .map(value -> value * 2)
            .filter(value -> value > 5)
            .subscribe(System.out::println);
    }
}
