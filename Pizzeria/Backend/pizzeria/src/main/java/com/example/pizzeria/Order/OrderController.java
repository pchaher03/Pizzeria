package com.example.pizzeria.Order;

import java.util.HashMap;

import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping(path = "orders")
public class OrderController {
    private final OrderService orderService;

    OrderController(OrderService orderService) {
        this.orderService = orderService;
    }

    @PostMapping("/addOrder")
    public ResponseEntity<Object> add(@RequestBody OrderRequest request) {
        HashMap<String, Object> map = new HashMap<String, Object>();

        try {
            map.put("mensaje", orderService.add(request));

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