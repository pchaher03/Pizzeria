package com.example.pizzeria.Auth;

import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.bind.annotation.RestController;

import java.util.HashMap;

import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.PutMapping;

@RestController
@RequestMapping(path = "auth")
public class AuthController {
    private final AuthService authService;

    public AuthController(AuthService authService) {
        this.authService = authService;
    }

    @PostMapping("/login")
    public ResponseEntity<Object> login(@RequestBody LoginRequest request) {
        HashMap<String, Object> map = new HashMap<String, Object>();

        try {
            map.put("token", authService.login(request));

            return new ResponseEntity<>(
                map,
                HttpStatus.ACCEPTED
            );
        } catch(Error error) {
            map.put("error", true);
            map.put("mensaje", error.getMessage());

            return new ResponseEntity<>(
                map,
                HttpStatus.CONFLICT
            );
        }
    }

    @PostMapping("/register")
    public ResponseEntity<Object> register(@RequestBody RegisterRequest request) {
        HashMap<String, Object> map = new HashMap<String, Object>();

        try {
            map.put("token", authService.register(request));

            return new ResponseEntity<>(
                map,
                HttpStatus.ACCEPTED
            );
        } catch(Error error) {
            map.put("error", true);
            map.put("mensaje", error.getMessage());

            return new ResponseEntity<>(
                map,
                HttpStatus.CONFLICT
            );
        }
    }

    @PutMapping("/updateAccount")
    @ResponseBody
    public ResponseEntity<Object> update(@RequestBody UpdateRequest request) {
        HashMap<String, Object> map = new HashMap<String, Object>();

        try {
            map.put("token", authService.update(request.getId(), request));
            map.put("mensaje", "Usuario actualizado");

            return new ResponseEntity<>(
                map,
                HttpStatus.ACCEPTED
            );
        } catch(Error error) {
            map.put("error", true);

            return new ResponseEntity<>(
                map,
                HttpStatus.CONFLICT
            );
        }
    }

    @DeleteMapping("/deleteAccount")
    public ResponseEntity<Object> delete(@RequestBody DeleteRequest request) {
        HashMap<String, Object> map = new HashMap<String, Object>();

        try {
            authService.delete(request.getId());
            map.put("mensaje", "Se borro la cuenta.");

            return new ResponseEntity<>(
                map,
                HttpStatus.ACCEPTED
            );
        } catch(Error error) {
            map.put("error", true);
            map.put("mensaje", error.getMessage());

            return new ResponseEntity<>(
                map,
                HttpStatus.CONFLICT
            );
        }
    }
}