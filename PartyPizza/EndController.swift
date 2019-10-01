//
//  EndController.swift
//  PartyPizza
//
//  Created by nithin muthukumar on 2019-09-29.
//  Copyright © 2019 nithin muthukumar. All rights reserved.
//

import UIKit

class EndController: UIViewController {

    override func viewDidLoad() {
        super.viewDidLoad()

        // Do any additional setup after loading the view.
    }
    
    @IBAction func End(_ sender: Any) {
        print(Globals.partyName)
        
        
        Commandler.makePost(["command":"delete_party","param":[Globals.partyName]])
    }
    
    /*
    // MARK: - Navigation

    // In a storyboard-based application, you will often want to do a little preparation before navigation
    override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
        // Get the new view controller using segue.destination.
        // Pass the selected object to the new view controller.
    }
    */

}
