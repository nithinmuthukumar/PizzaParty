//
//  ToppingSelectController.swift
//  PartyPizza
//
//  Created by nithin muthukumar on 2019-09-29.
//  Copyright © 2019 nithin muthukumar. All rights reserved.
//

import UIKit

class ToppingSelectController: UIViewController,UITextFieldDelegate {
    @IBOutlet weak var NameField: UITextField!
    var toppings=["Green Peppers":false,"Mushrooms":false,"Pepperoni":false,"Onions":false,"Black Olives":false,"Jalapenos":false,"Banana Peppers":false,"Bacon":false,"Beef":false,"Ham":false,"Extra Cheese":false]
    

    @IBAction func GP(_ sender: Any) {
        if(toppings["Green Peppers"]!){
            toppings["Green Peppers"]=false
            
        }
        else{
            toppings["Green Peppers"]=true
        }
        
        
    }
    
    @IBAction func Mush(_ sender: Any) {
        if(toppings["Mushrooms"]!){
            toppings["Mushrooms"]=false
            
        }
        else{
            toppings["Mushrooms"]=true
        }
    }
    
    @IBAction func Pep(_ sender: Any) {
        if(toppings["Pepperoni"]!){
            toppings["Pepperoni"]=false
            
        }
        else{
            toppings["Pepperoni"]=true
        }
    }
    
    @IBAction func Oni(_ sender: Any) {
        if(toppings["Onions"]!){
            toppings["Onions"]=false
            
        }
        else{
            toppings["Onions"]=true
        }
    }
    @IBAction func Bo(_ sender: Any) {
        if(toppings["Black Olives"]!){
            toppings["Black Olives"]=false
            
        }
        else{
            toppings["Black Olives"]=true
        }
        
    }
    @IBAction func Jala(_ sender: Any) {
        if(toppings["Jalapenos"]!){
            toppings["Jalapenos"]=false
            
        }
        else{
            toppings["Jalapenos"]=true
        }
    }
    
    @IBAction func BP(_ sender: Any) {
        if(toppings["Banana Peppers"]!){
            toppings["Banana Peppers"]=false
            
        }
        else{
            toppings["Banana Peppers"]=true
        }
    }
    @IBAction func Bac(_ sender: Any) {
        if(toppings["Bacon"]!){
            toppings["Bacon"]=false
            
        }
        else{
            toppings["Bacon"]=true
        }
    }
    @IBAction func Ham(_ sender: Any) {
        if(toppings["Ham"]!){
            toppings["Ham"]=false
            
        }
        else{
            toppings["Ham"]=true
        }
    }
    @IBAction func Beef(_ sender: Any) {
        if(toppings["Beef"]!){
            toppings["Beef"]=false
            
        }
        else{
            toppings["Beef"]=true
        }
    }
    @IBAction func EC(_ sender: Any) {
        if(toppings["Extra Cheese"]!){
            toppings["Extra Cheese"]=false
            
        }
        else{
            toppings["Extra Cheese"]=true
        }
    }
    
    override func viewDidLoad() {
        super.viewDidLoad()
        NameField.delegate=self

        // Do any additional setup after loading the view.
    }
    

    func textFieldShouldReturn(_ textField: UITextField) -> Bool {
        textField.resignFirstResponder()
        return true
    }

    @IBAction func Create(_ sender: Any) {
        Globals.pizzas.append((NameField.text!,toppings))
        
    }
    

}
