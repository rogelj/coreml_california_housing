//
//  ContentView.swift
//  CaliforniaPricer
//
//  Created by J. Rogel on 25/12/2025.
//

import SwiftUI

struct ContentView: View {
    var body: some View {
        VStack {
            Text("California Pricer").font(.largeTitle)
        }
        .padding()
        HStack {
            Text("Median Income (USD)").padding(.trailing, 40)
            Text("No. of  Rooms").padding(.leading, 40)
        }
    }
}

#Preview {
    ContentView()
}
