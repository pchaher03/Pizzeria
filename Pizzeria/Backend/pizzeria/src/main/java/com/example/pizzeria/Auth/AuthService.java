package com.example.pizzeria.Auth;
import java.util.HashMap;
import java.util.Optional;

import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.security.authentication.AuthenticationManager;
import org.springframework.security.authentication.UsernamePasswordAuthenticationToken;
import org.springframework.security.core.userdetails.UserDetails;
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
    private final AuthenticationManager authenticationManager;
    public AuthService(UserRepository userRepository, JwtService jwtService, PasswordEncoder passwordEncoder, AuthenticationManager authenticationManager) {
        this.userRepository = userRepository;
        this.jwtService = jwtService;
        this.passwordEncoder = passwordEncoder;
        this.authenticationManager = authenticationManager;
    }
    public String login(LoginRequest request) {
        authenticationManager.authenticate(
            new UsernamePasswordAuthenticationToken(
                request.getEmail(),
                request.getPassword())
        );
        User user=userRepository.findUserByEmail(request.getEmail()).orElseThrow();
        String token = jwtService.getToken(user);
        return token;
    }
    public String register(RegisterRequest request) {
        Optional<User> res = userRepository.findUserByEmail(request.getEmail());
        if(res.isPresent()) {
            throw new Error("Ya existe una cuenta con ese email.");
        }
        User user = new User(
            request.getEmail(),
            passwordEncoder.encode(request.getPassword()),
            request.getFirstName(),
            request.getLastName(),
            request.getCellphone(),
            Role.USER
        );
        userRepository.save(user);
        return jwtService.getToken(user);
    }
    public String update(User request) {
        Optional<User> res = userRepository.findById(request.getId());
        if (res.isPresent()) {
            User existingUser = res.get();

            existingUser.setPassword(passwordEncoder.encode(request.getPassword()));
            existingUser.setFirstName(request.getFirstName());
            existingUser.setLastName(request.getLastName());
            existingUser.setCellphone(request.getCellphone());

            // Actualizar solo los campos que han cambiado
            // if (request.getPassword() != null && !request.getPassword().isEmpty()) {
            //     existingUser.setPassword(passwordEncoder.encode(request.getPassword()));
            // }
            // if (request.getEmail() != null && !request.getEmail().isEmpty()) {
            //     existingUser.setEmail(request.getEmail());
            // }
            // if (request.getFirstName() != null && !request.getFirstName().isEmpty()) {
            //     existingUser.setFirstName(request.getFirstName());
            // }
            // if (request.getLastName() != null && !request.getLastName().isEmpty()) {
            //     existingUser.setLastName(request.getLastName());
            // }
            // if (request.getCellphone() != null && !request.getCellphone().isEmpty()) {
            //     existingUser.setCellphone(request.getCellphone());
            // }

            // Guardar el usuario actualizado
            userRepository.save(existingUser);

            return "Se guardó el usuario con éxito.";
        } else {
            throw new RuntimeException("Usuario no encontrado.");
        }
    }
    public ResponseEntity<Object> delete(Long id) {
        Boolean exists = this.userRepository.existsById(id);
        HashMap<String, Object> map = new HashMap<>();
        if(!exists) {
            map.put("error", true);
            map.put("mensaje", "No existe una cuenta con ese id.");
            return new ResponseEntity<>(
                map,
                HttpStatus.CONFLICT
            );
        } else {
            userRepository.deleteById(id);
            map.put("mensaje", "Cuenta eliminada.");
            return new ResponseEntity<>(
                map,
                HttpStatus.ACCEPTED
            );
        }
    }
}