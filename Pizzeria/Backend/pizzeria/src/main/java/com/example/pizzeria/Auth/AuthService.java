package com.example.pizzeria.Auth;
import java.util.Optional;
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
        UserDetails user=userRepository.findUserByEmail(request.getEmail()).orElseThrow();
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
}