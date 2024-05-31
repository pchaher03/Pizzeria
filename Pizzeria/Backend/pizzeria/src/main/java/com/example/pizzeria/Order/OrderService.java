package com.example.pizzeria.Order;
import org.springframework.stereotype.Service;
@Service
public class OrderService {
    OrderRepository orderRepository;
    OrderService(OrderRepository orderRepository) {
        this.orderRepository = orderRepository;
    }
    public String add(OrderRequest request) {
        Order order = new Order(
            request.getUserId(),
            request.getPizza(),
            request.getPrice()
        );
        orderRepository.save(order);
        return "Orden realizada con exito.";
    }
}