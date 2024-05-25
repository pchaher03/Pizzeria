package com.example.pizzeria.User;

import jakarta.persistence.*;

@Entity
@Table(name = "users")
public class User {
    @Id
	@GeneratedValue(strategy =  GenerationType.IDENTITY)
	private Long id;
	
	@Column(name = "first_name")
	private String firstName;
	
	@Column(name = "last_name")
	private String lastName;

	@Column(name = "cellphone")
	private String cellphone;
	
	@Column(name = "email", unique = true)
	private String email;

    @Column(name = "password")
    private String password;

	public User() {};

	public User(String firstName, String lastName, String cellphone, String email, String password) {
        this.firstName = firstName;
        this.lastName = lastName;
		this.cellphone = cellphone;
        this.email = email;
		this.password = password;
    }

	public User(Long id, String firstName, String lastName, String cellphone, String email, String password) {
		this.id = id;
        this.firstName = firstName;
        this.lastName = lastName;
		this.cellphone = cellphone;
        this.email = email;
		this.password = password;
    }
    
	public long getId() {
		return id;
	}
	public void setId(long id) {
		this.id = id;
	}
	public String getFirstName() {
		return firstName;
	}
	public void setFirstName(String first_name) {
		this.firstName = first_name;
	}
	public String getLastName() {
		return lastName;
	}
	public void setLastName(String last_name) {
		this.lastName = last_name;
	}
	public String getCellphone() {
		return cellphone;
	}
	public void setCellphone(String cellphone) {
		this.cellphone = cellphone;
	}
	public String getEmail() {
		return email;
	}
	public void setEmail(String email) {
		this.email = email;
	}
	public String getPassword() {
		return password;
	}
	public void setPassword(String password) {
		this.password = password;
	}
}
