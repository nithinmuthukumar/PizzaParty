//
//  PizzaSelectController.swift
//  PartyPizza
//
//  Created by nithin muthukumar on 2019-09-29.
//  Copyright © 2019 nithin muthukumar. All rights reserved.
//

import UIKit

class PizzaSelectController: UIViewController,UITableViewDelegate,UITableViewDataSource {
    @IBOutlet weak var TableView: UITableView!
    @IBOutlet weak var menter: UIStepper!
    @IBAction func IncrementOrDecrement(_ sender: Any, forEvent event: UIEvent) {
        if let selected=TableView.indexPathForSelectedRow{
            let label=TableView.cellForRow(at: selected)?.textLabel!
            label?.text=(label?.text?.split(separator: " ")[0])!+" x"+String(Int(menter.value))
            
            
        }
        
        
    }
    @IBOutlet weak var FinishButton: UIButton!
    func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        
        return Globals.shrooms.count
    }
    
    @IBAction func FinishPlease(_ sender: Any) {
        Commandler.makePost(["command":"create_new_party","toppings":["pepperoni"]])
    }
    func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        let cell=tableView.dequeueReusableCell(withIdentifier: "Pizza",for: indexPath)
        // your cell coding
        
        cell.textLabel?.text=Globals.shrooms[indexPath.row].split(separator: " ")[0]+" 0"
        return cell
    }
    

    override func viewDidLoad() {
        super.viewDidLoad()
        TableView.delegate=self
        TableView.dataSource=self

        
    }

}
