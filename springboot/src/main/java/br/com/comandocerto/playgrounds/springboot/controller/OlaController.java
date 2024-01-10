package br.com.comandocerto.playgrounds.springboot.controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ResponseBody;

@Controller
public class OlaController {

    @GetMapping("/ola-mundo")
    @ResponseBody
    public String olaMundo() {
        return "Olá mundo!";
    }
}