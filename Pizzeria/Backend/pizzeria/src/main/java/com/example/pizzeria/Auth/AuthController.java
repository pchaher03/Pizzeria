package com.example.pizzeria.Auth;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.bind.annotation.RestController;

import com.example.pizzeria.User.User;

import java.util.HashMap;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.PathVariable;
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
    @PutMapping("/updateAccount/{userId}")
    @ResponseBody
    public ResponseEntity<Object> update(@PathVariable("userId") String userId, @RequestBody User user) {
        HashMap<String, Object> map = new HashMap<String, Object>();
        try {
            //Long prueba = Long.parseLong(userId);

            user.setId(Long.parseLong(userId));
            map.put("datos", authService.update(user));
            map.put("mensaje", "Usuario actualizado");
            return new ResponseEntity<>(
                map,
                HttpStatus.ACCEPTED
            );
        } catch(Error error) {
            map.put("error", true);
            map.put("mensaje", userId);
            return new ResponseEntity<>(
                map,
                HttpStatus.CONFLICT
            );
        }
    }
    @PostMapping("/deleteAccount")
    public ResponseEntity<Object> delete(@RequestBody RegisterRequest request) {
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