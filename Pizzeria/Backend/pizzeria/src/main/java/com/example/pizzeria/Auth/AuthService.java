package com.example.pizzeria.Auth;

import java.util.HashMap;
import java.util.Optional;

import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.stereotype.Service;

import com.example.pizzeria.Jwt.JwtService;
import com.example.pizzeria.User.Role;
import com.example.pizzeria.User.User;
import com.example.pizzeria.User.UserRepository;


@Service
public class AuthService {
    private final UserRepository userRepository;
    private final JwtService jwtService;
    private final PasswordEncoder passwordEncoder;
    public AuthService(UserRepository userRepository, JwtService jwtService, PasswordEncoder passwordEncoder) {
        this.userRepository = userRepository;
        this.jwtService = jwtService;
        this.passwordEncoder = passwordEncoder;
    }
    public AuthResponse login(LoginRequest request) {
        return null;
    }
    public String register(RegisterRequest request) {
        Optional<User> res = userRepository.findUserByEmail(request.getEmail());
        if(res.isPresent()) {
            throw new Error("Ya existe una cuenta con ese email.");
        }
        User user = new User(
            request.getEmail(),
            request.getPassword(),
            request.getFirstName(),
            request.getLastName(),
            request.getCellphone(),
            Role.USER
        );
        userRepository.save(user);
        return jwtService.getToken(user);
    }
}
