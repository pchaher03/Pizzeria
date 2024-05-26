package com.example.pizzeria.Auth;

import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.HashMap;

import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;

@RestController
@RequestMapping(path = "auth")
public class AuthController {
    private final AuthService authService;
    private final HashMap<String, Object> map;

    public AuthController(AuthService authService) {
        this.authService = authService;
        map = new HashMap<>();
    }

    @PostMapping("/login")
    public ResponseEntity<AuthResponse> login(@RequestBody LoginRequest request) {

        return ResponseEntity.ok(authService.login(request));
    }

    @PostMapping("/register")
    public ResponseEntity<Object> register(@RequestBody RegisterRequest request) {
        map.clear();
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
    
}
