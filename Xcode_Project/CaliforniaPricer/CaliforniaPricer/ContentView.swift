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
            Text("Median Income (USD)").padding(.trailing, 10)
            Text("No. of  Rooms").padding(.leading, 10)
        }
        .padding(.vertical, 40)
        Button(action: {}) {
            Text("Get Prediction")
        }
    }
}

#Preview {
    ContentView()
}
