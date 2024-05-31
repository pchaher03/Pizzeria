package com.example.pizzeria.Order;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface OrderRepository extends JpaRepository<Order, Long> {
    //Optional<Order> findById(Long id);
    //Optional<Order> findByUser(Long id);
}
