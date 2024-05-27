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
}