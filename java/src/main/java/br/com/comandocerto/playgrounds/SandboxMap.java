package br.com.comandocerto.playgrounds;

import java.util.HashMap;
import java.util.Map;

public class SandboxMap {
    public static void main(String[] args) {
        Map<Integer, String> map = new HashMap<Integer, String>();
        map.put(1,"Um");
        map.put(2,"Dois");
        System.out.println(map.get(1));
        System.out.println(map.get(2));
    }
}
