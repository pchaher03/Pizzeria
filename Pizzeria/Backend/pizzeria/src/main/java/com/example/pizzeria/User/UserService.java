package com.example.pizzeria.User;

import java.util.HashMap;
import java.util.List;
import java.util.Optional;

import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Service;

@Service
public class UserService {
    private final UserRepository userRepository;
    public UserService(UserRepository userRepository) {
        this.userRepository = userRepository;
    }
    public List<User> getUsers() {
        return this.userRepository.findAll();
    }
    public ResponseEntity<Object> registerUser(User user) {
        Optional<User> res = userRepository.findUserByEmail(user.getEmail());
        HashMap<String, Object> map = new HashMap<>();
        if(res.isPresent()) {
            map.put("error", true);
            map.put("mensaje", "Ya existe una cuenta con ese email.");
            return new ResponseEntity<>(
                map,
                HttpStatus.CONFLICT
            );
        }
        userRepository.save(user);
        map.put("datos", user);
        map.put("mensaje", "La cuenta se creo con exito.");
        return new ResponseEntity<>(
            map,
            HttpStatus.CREATED
        );
    }

    public ResponseEntity<Object> updateUser(User user) {
        Optional<User> res = userRepository.findById(user.getId());
        HashMap<String, Object> map = new HashMap<>();
        if(res.isPresent()) {
            userRepository.save(user);
            map.put("datos", user);
            map.put("mensaje", "La cuenta se actualizo con exito.");
            return new ResponseEntity<>(
                map,
                HttpStatus.ACCEPTED
            );
        }
        else {
            map.put("error", true);
            map.put("mensaje", "No existe una cuenta con ese id.");
            return new ResponseEntity<>(
                map,
                HttpStatus.CONFLICT
            );
        }
    }

    public ResponseEntity<Object> deleteUser(Long id) {
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
